				org			$4
Vector_001		dc.l		Main
				org			$500
			
Main			movea.l		#String1,a0
				jsr			RemoveSpace	;fonctionne
				jsr			GetExpr	;fonctionne
				
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
				cmpi.b		#'7',(a0)+
				bhi			\True
				tst.b		(a0)
				bne			\True
				bra			\False
				
				
\False			andi.b  	#%11111011,ccr  ; Positionne le flag Z à 0 (false)
				bra			\quit
				
\True			ori.b   	#%00000100,ccr  ; Positionne le flag Z à 1 (true)

\quit			movem.l		(a7)+,d0/a0
				rts

Convert			tst.b		(a0)
				beq			\error
				jsr			IsCharError
				beq			\error
				jsr			IsMaxError
				beq			\error
				jsr			Atoui
				bra			\true
						
\error			andi.b  	#%11111011,ccr  ; Positionne le flag Z à 0 (false)
				jsr			\quit

\true			ori.b		#%00000100,ccr  ; Positionne le flag Z à 1 (true)

\quit			rts
		
Atoui			movem.l	a0/d1,-(a7)
				clr.l	d0
				clr.l	d1
				
\loop			move.b	(a0)+,d1
				beq		\quit
				subi.w	#'0',d1
				mulu.w	#10,d0
				add.w	d1,d0
				bra		\loop
							
\quit			movem.l	(a7)+,d1/a0
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


GetNum 			movem.l 	d1/a1-a2,-(a7)
				movea.l 	a0,a1
				jsr 		NextOp
				movea.l 	a0,a2
				move.b 		(a2),d1
				clr.b 		(a2)
				movea.l 	a1,a0
				jsr 		Convert
				beq 		\true
				
\false 			move.b 		d1,(a2)
				andi.b 		#%11111011,ccr
				bra 		\quit
				
\true 			move.b 		d1,(a2)
				movea.l 	a2,a0
				ori.b 		#%00000100,ccr
				
\quit 			movem.l 	(a7)+,d1/a1-a2
				rts
				
				
GetExpr 		movem.l 	d1-d2/a0,-(a7)
				jsr 		GetNum
				bne 		\false
				move.l 		d0,d1
				
\loop 			move.b 		(a0)+,d2
				beq 		\true
				jsr 		GetNum
				bne 		\false
				cmp.b 		#'+',d2
				beq 		\addition
				cmp.b 		#'-',d2
				beq 		\subtract
				cmp.b 		#'*',d2
				beq 		\multiply
				bra 		\divide
				
				
\addition		add.l 		d0,d1
				bra 		\loop
\subtract 		sub.l 		d0,d1
				bra 		\loop
\multiply 		muls.w 		d0,d1
				bra 		\loop
\divide 		tst.w 		d0
				beq 		\false
				divs.w		d0,d1
				ext.l 		d1
				bra 		\loop
\false 			andi.b 		#%11111011,ccr
				bra 		\quit
\true 			move.l 		d1,d0
				ori.b 		#%00000100,ccr
\quit 			movem.l 	(a7)+,d1-d2/a0
				rts
				
Uitoa 			; Sauvegarde les registres.
				movem.l 	d0/a0,-(a7)
				; Empile le caractère nul de fin de chaîne.
				clr.w 		-(a7)
\loop 			; Limite D0 à 16 bits pour la division (seuls les 16 bits de
				; poids faible contiennent le nombre à diviser).
				andi.l 		#$ffff,d0
				; Divise D0 par 10 afin de récupérer le reste.
				; Le quotient est placé dans les 16 bits de poids faible.
				; Le reste est placé dans les 16 bits de poids fort.
				divu.w 		#10,d0
				; Fait passer le reste dans les 16 bits de poids faible.
				; (Le quotient passe dans les 16 bits de poids fort.)
				swap 		d0
				; Convertit le reste en caractère ASCII (sur 8 bits).
				addi.b 		#'0',d0
				; Empile le caractère ASCII (sur 16 bits).
				move.w 		d0,-(a7)
				; Fait repasser le quotient dans les 16 bits de poids faible.
				swap 		d0
				; Si le quotient n'est pas nul,
				; il reste des chiffres à convertir.
				; On passe donc au chiffre suivant.
				tst.w 		d0
				bne 		\loop
				; Sinon tous les chiffres ont été traités,
				; il ne reste plus qu'à les écrire dans la chaîne.
\writeChar 		; Dépile le caractère (sur 16 bits).
				move.w 		(a7)+,d0
				; Puis l'écrit dans la chaîne (sur 8 bits).
				move.b 		d0,(a0)+
				; Continue tant que le caractère n'est pas nul.
				bne 		\writeChar
				; Restaure les registres puis sortie.
				movem.l 	(a7)+,d0/a0
				rts


String1			dc.b	"1 2+ 35 ",0
