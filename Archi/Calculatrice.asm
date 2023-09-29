				org			$4
Vector_001		dc.l		Main
				org			$500
			
Main			movea.l		#String2,a0
				;jsr			RemoveSpace	;fonctionne
				;jsr			IsCharError	;fonctionne
				jsr			IsMaxError
				illegal
			
RemoveSpace		movem.l		a0/a1/d0,-(a7)
				clr.l		d0
				movea.l		a0,a1

\loop			move.b		(a1)+,d0
				tst.b		d0
				beq			\quit
				cmpi.b		#' ',d0
				beq			\loop
				move.b		d0,(a0)
				addq.l		#1,a0
				bra			\loop
				
\quit			move.b		d0,(a0)
				movem.l		(a7)+,d0/a1/a0
				rts
				
				
				
				
				
				
				
IsCharError		movem.l		a0/d0,-(a7)
				clr.l		d0
				
\loop			move.b		(a0)+,d0
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

\Quit			movem.l		(a7)+,d0/a0
				rts
				
				
				
				
				
				
				
				
				
				
				
				
				
				
IsMaxError		movem.l		a0/d0,-(a7)
				clr.l		d0
				jsr			StrLen
				cmpi.l		#5,d0
				blo			\False
				cmpi.b		#5,d0
				bhi			\True
				bra			\max
				
\max			cmpi.b		#'3',(a0)+
				bhi			\True
				cmpi.b		#'2',(a0)+
				bhi			\True
				cmpi.b		#'7',(a0)+
				bhi			\True
				cmpi.b		#'6',(a0)+
				bhi			\True
				cmpi.b		#'7',(a1)+
				bhi			\True
				tst.b		(a1)
				bne			\True
				bra			\False
				
				
\False			andi.b  	#%11111011,ccr  ; Positionne le flag Z à 0 (false)
				bra			\quit
				
\True			ori.b   	#%00000100,ccr  ; Positionne le flag Z à 1 (true)

\quit			movem.l		(a7)+,d0/a0
				rts
				
				
				

StrLen			movem.l		a0/d0,-(a7)
				clr.l		d0
			
\loop			tst.b		(a0)+
				beq			\quit
			
				addq.l		#1,d0
				bra			\loop
			
\quit			movea.l		(a7)+,a0
				rts		

String1			dc.b	"1  2+3 5",0
String2			dc.b	"32",0
