				org			$0
Vector_000		dc.l		$ffb500
Vector_001		dc.l		Main
				org			$500
			
Main			movea.l		#String1,a0
				jsr			RemoveSpace	;fonctionne
				jsr			GetNum
				
				illegal
			
RemoveSpace		movem.l		a0/a1/d0,-(a7)
				movea.l		a0,a1

\loop			move.b		(a1)+,d0
				beq			\quit
				cmpi.b		#' ',d0
				beq			\loop
				move.b		d0,(a0)+
				bra			\loop
				
\quit			move.b		d0,(a0)
				movem.l		(a7)+,d0/a1/a0
				rts
				

				
StrLen			movem.l		a0/d1,-(a7)
			
\loop			move.b		(a0)+,d1
				beq			\quit
			
				addq.l		#1,d0
				bra			\loop
			
\quit			movem.l		(a7)+,d1/a0
				rts			
				
				
				
				
				
IsCharError		movem.l		a1/d0,-(a7)
				clr.l		d0
				
\loop			move.b		(a1)+,d0
				tst.b		d0
				beq			\False
				cmpi.b		#'0',d0
				blo			\True
				cmpi.b		#'9',d0
				bhi			\True
				bra			\loop
				
				
\False			andi.b  	#%11111011,ccr  ; Positionne le flag Z à 0 (false)
				bra			\Quit
				
\True			ori.b   	#%00000100,ccr  ; Positionne le flag Z à 1 (true)
				bra			\Quit

\Quit			movem.l		(a7)+,d0/a1
				rts	
				

				
				
				
				
IsMaxError		movem.l		a1/d0,-(a7)
				clr.l		d0
				jsr			StrLen
				cmpi.l		#5,d0
				blo			\False
				cmpi.b		#5,d0
				bhi			\True
				bra			\max
				
\max			cmpi.b		#'3',(a1)+
				bhi			\True
				cmpi.b		#'2',(a1)+
				bhi			\True
				cmpi.b		#'7',(a1)+
				bhi			\True
				cmpi.b		#'6',(a1)+
				bhi			\True
				cmpi.b		#'7',(a1)+
				bhi			\True
				tst.b		(a1)
				bne			\True
				bra			\False
				
				
\False			andi.b  	#%11111011,ccr  ; Positionne le flag Z à 0 (false)
				bra			\quit
				
\True			ori.b   	#%00000100,ccr  ; Positionne le flag Z à 1 (true)

\quit			movem.l		(a7)+,d0/a1
				rts

Convert			tst.b		(a1)
				beq			\error
				jsr			IsCharError
				beq			\error
				jsr			IsMaxError
				beq			\error
				jsr			Atoui
				bra			\true
						
\error			andi.b  	#%11111011,ccr  ; Positionne le flag Z à 0 (false)
				jsr			\quit

\true			ori.b		   	#%00000100,ccr  ; Positionne le flag Z à 1 (true)

\quit			rts
		
Atoui			movem.l	a1/d1,-(a7)
				clr.l	d1
				
\loop			move.b	(a1)+,d1
				tst.b	d1
				beq		\quit
				subi.w	#'0',d1
				mulu.w	#10,d0
				add.w	d1,d0
				bra		\loop
							
\quit			movem.l	(a7)+,d1/a1
				rts
				
				
Print			movem.l	a0/d1/d0,-(a7)
				clr.l	d0

\loop			move.b	(a0)+,d0
				tst.b	d0
				beq		\quit
				jsr		PrintChar
				addi.l	#1,d1
				bra		\loop
				
\quit			movem.l	(a7)+,d0/d1/a0
				rts			
				


PrintChar		incbin	"PrintChar.bin"


NextOp			tst.b	(a0)
				beq		\quit
				cmpi.b	#'+',(a0)
				beq		\quit
				cmpi.b	#'-',(a0)
				beq		\quit
				cmpi.b	#'*',(a0)
				beq		\quit
				cmpi.b	#'%',(a0)
				beq		\quit
				addq.l	#1,a0
				bra		NextOp

\quit			rts

GetNum			movem.l		a1/a2,-(a7)
				move.l		a0,a1
				move.l		a0,a2
				jsr			NextOp			; a0 pointe sur la première opérande
				move.b		(a0),d1			; on conserve l'opérande
				move.b		0,(a0)			; on le remplace par Null
				jsr			Convert			; ??? et conserve le premier nombre dans d0
				bne			\false			; s'il y a un pb
				bra			\quit			; sinon
				
\false			andi.b  	#%11111011,ccr  ; Positionne le flag Z à 0 (false)
				move.b		d1,(a0)
				move.l		a1,a0
				bra			\quit
				
\quit			movem.l		(a7)+,a2/a1
				move.b		d1,(a0)
				rts
				

	

String1			dc.b	"1 2 +  35",0
