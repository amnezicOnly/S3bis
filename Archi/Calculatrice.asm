				org			$4
Vector_001		dc.l		Main
				org			$500
			
Main			movea.l		#String1,a0
				jsr			RemoveSpace	;fonctionne
				jsr			GetExpr
				
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
				
GetExpr 		; Sauvegarde les registres.
				movem.l 	d1-d2/a0,-(a7)
				; Conversion du premier nombre de l'expression (dans D0).
				; Si erreur, on renvoie false.
				jsr 		GetNum
				bne 		\false
				; Le premier nombre est chargé dans D1.
				; (D1 contiendra le résultat des opérations successives.)
				move.l 		d0,d1
\loop 			; L'opérateur ou le caractère nul est copié dans D2.
				; S'il s'agit du caractère nul, on renvoie true (pas d'erreur).
				move.b 		(a0)+,d2
				beq 		\true
				; Conversion du prochain nombre (dans D0).
				; Si erreur, on renvoie false.
				jsr 		GetNum
				bne 		\false
				; Détermine le type de l'opération (+, -, *, /).
				cmp.b 		#'+',d2
				beq 		\addition
				cmp.b 		#'-',d2
				beq 		\subtract
				cmp.b 		#'*',d2
				beq 		\multiply
				bra 		\divide
				; Effectue l'opération puis passe au nombre suivant.
\addition		add.l 		d0,d1
				bra 		\loop
\subtract 		sub.l 		d0,d1
				bra 		\loop
\multiply 		muls.w 		d0,d1
				bra 		\loop
\divide 		; Renvoie une erreur si une division par zéro est détectée.
				tst.w 		d0
				beq 		\false
				; Le résultat entier de la division est sur 16 bits. Il faut
				; réaliser une extension de signe pour l'avoir sur 32 bits.
				divs.w		d0,d1
				ext.l 		d1
				bra 		\loop
\false 			; Sortie avec erreur (Z = 0).
				andi.b 		#%11111011,ccr
				bra 		\quit
\true 			; Sortie sans erreur (Z = 1).
				; (Avec la copie du résultat dans D0.)
				move.l 		d1,d0
				ori.b 		#%00000100,ccr
\quit 			; Restaure les registres puis sortie.
				movem.l 	(a7)+,d1-d2/a0
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
				

	

String1			dc.b	"1 2 +  35",0
