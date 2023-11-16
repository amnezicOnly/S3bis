				org			$4
Vector_001		dc.l		Main
				org			$500
				
Main			movea.l		#String1,a0
				jsr			RemoveSpace	;fonctionne
				jsr			GetNum
				illegal


StrLen			move.l		a0,-(a7)
				clr.l		d0

\loop			tst.b		(a0)+
				beq			\quit
				addq.l		#1,d0
				bra			\loop
				
\quit			move.l		(a7)+,a0
				rts

Atoui 			; Sauvegarde les registres dans la pile.
				movem.l d1/a0,-(a7)
				; Initialise la variable de retour à 0.
				clr.l d0
				; Initialise la variable de conversion à 0.
				clr.l d1
\loop 			; On copie le caractère courant dans D1
				; A0 pointe ensuite sur le caractère suivant (post incrémentation).
				move.b (a0)+,d1
				; Si le caractère copié est nul,
				; on quitte (fin de chaîne).
				beq \quit
				; Sinon, on réalise la conversion numérique du caractère.
				subi.b #'0',d1
				; On décale la variable de retour vers la gauche (x10),
				; puis on y ajoute la valeur numérique du caractère.
				mulu.w #10,d0
				add.l d1,d0
				; Passage au caractère suivant.
				bra \loop
\quit 			; Restaure les registres puis sortie.
				movem.l (a7)+,d1/a0
				rts

RemoveSpace 	; Sauvegarde les registres dans la pile.
				movem.l 	d0/a0/a1,-(a7)
				; Fait pointer A1 sur la chaîne destination.
				; (Même chaîne que la source.)
				movea.l 	a0,a1
\loop 			; Charge un caractère de la chaîne dans D0 et incrémente A0.
				move.b 		(a0)+,d0
				; Si le caractère est un espace, saut à \loop.
				cmpi.b 		#' ',d0
				beq 		\loop
				; Sinon, on copie le caractère dans la destination
				; et on incrémente le pointeur destination.
				; Si le caractère qui vient d'être copié n'est pas nul,
				; saut à loop.
				move.b 		d0,(a1)+
				bne 		\loop
				
\quit 			; Restaure les registres puis sortie.
				movem.l		(a7)+,d0/a0/a1
				rts

IsCharError 	; Sauvegarde les registres dans la pile.
				movem.l 	d0/a0,-(a7)
\loop 			; Charge un caractère de la chaîne dans D0 et incrémente A0.
				; Si le caractère est nul, on renvoie false (pas d'erreur).
				move.b 		(a0)+,d0
				beq 		\false
				; Compare le caractère au caractère '0'.
				; S'il est inférieur, on renvoie true (ce n'est pas un chiffre).
				cmpi.b 		#'0',d0
				blo 		\true
				; Compare le caractère au caractère '9'.
				; S'il est inférieur ou égal, on reboucle (c'est un chiffre).
				; S'il est supérieur, on renvoie true (ce n'est pas un chiffre).
				cmpi.b 		#'9',d0
				bls 		\loop
\true 			; Sortie qui renvoie Z = 1 (erreur).
				; (L'instruction BRA ne modifie pas le flag Z.)
				ori.b 		#%00000100,ccr
				bra 		\quit
\false 			; Sortie qui renvoie Z = 0 (aucune erreur).
				andi.b 		#%11111011,ccr
\quit 			; Restaure les registres puis sortie.
				; (Les instructions MOVEM et RTS ne modifient pas le flag Z.)
				movem		(a7)+,d0/a0
				rts
				
IsMaxError 		; Sauvegarde les registres dans la pile.
				movem.l 	d0/a0,-(a7)
				; On récupère la taille de la chaîne (dans D0).
				jsr 		StrLen
				; Si la chaîne a plus de 5 caractères, renvoie true (erreur).
				; Si la chaîne a moins de 5 caractères, renvoie false (pas d'erreur).
				cmpi.l 		#5,d0
				bhi \true
				blo \false
				; Si la chaîne contient exactement 5 caractères :
				; comparaisons successives avec '3', '2', '7', '6' et '7'.
				; Si supérieur, on quitte en renvoyant une erreur.
				; Si inférieur, on quitte sans renvoyer d'erreur.
				; Si égal, on compare le caractère suivant.
				cmpi.b 		#'3',(a0)+
				bhi 		\true
				blo 		\false
				cmpi.b 		#'2',(a0)+
				bhi 		\true
				blo 		\false
				cmpi.b 		#'7',(a0)+
				bhi 		\true
				blo 		\false
				cmpi.b 		#'6',(a0)+
				bhi 		\true
				blo 		\false
				cmpi.b		 #'7',(a0)
				bhi 		\true
\false 			; Sortie qui renvoie Z = 0 (aucune erreur).
				; (L'instruction BRA ne modifie pas le flag Z.)
				andi.b 		#%11111011,ccr
				bra 		\quit
\true 			; Sortie qui renvoie Z = 1 (erreur).
				ori.b 		#%00000100,ccr
\quit 			; Restaure les registres puis sortie.
				; (Les instructions MOVEM et RTS ne modifient pas le flag Z.)
				movem.l 	(a7)+,d0/a0
				rts
				
				
				
Convert 		; Si la chaîne est nulle,
				; on quitte en renvoyant false (erreur).
				tst.b 		(a0)
				beq 		\false
				; (À ce stade, la chaîne n'est pas nulle.)
				; S'il existe une erreur sur les caractères,
				; on quitte en renvoyant false (erreur).
				jsr 		IsCharError
				beq 		\false
				; (À ce stade, la chaîne n'est pas nulle
				; et ne contient que des chiffres.)
				; Si le nombre que contient la chaîne est supérieur à 32767,
				; on quitte en renvoyant false (erreur).
				jsr 		IsMaxError
				beq 		\false
				; La chaîne est valide, il ne reste plus qu'à la convertir
				; puis à quitter en renvoyant true (aucune erreur).
				jsr 		Atoui
\true 			; Sortie qui renvoie Z = 1 (aucune erreur).
				ori.b 		#%00000100,ccr
				rts
\false 			; Sortie qui renvoie Z = 0 (erreur).
				andi.b 		#%11111011,ccr
				rts
				
NextOp 			; Si le caratère est nul (fin de chaîne),
				; il n'y a pas d'opérateur dans la chaîne.
				; A0 pointe sur le caractère nul. On quitte.
				tst.b 		(a0)
				beq 		\quit
				; Comparaisons successives du caractère aux 4 opérateurs.
				; Si le caractère est un opérateur, on peut quitter.
				; (A0 contient l'adresse de l'opérateur.)
				cmpi.b 		#'+',(a0)
				beq 		\quit
				cmpi.b 		#'-',(a0)
				beq 		\quit
				cmpi.b 		#'*',(a0)
				beq 		\quit
				cmpi.b 		#'/',(a0)
				beq 		\quit
				; Passage au caractère suivant.
				addq.l 		#1,a0
				bra 		NextOp
\quit 			; Sortie.
				rts
				
				
GetNum 			; Sauvegarde les registres.
				movem.l 	d1/a1-a2,-(a7)
				; Mémorise le début de la chaîne dans A1.
				movea.l 	a0,a1
				; Cherche le prochain opérateur ou le caractère nul
				; (c'est-à-dire le caractère qui suit le nombre),
				; et mémorise sa position dans A2.
				jsr 		NextOp
				movea.l 	a0,a2
				; Sauvegarde l'opérateur ou le caractère nul dans D1.
				move.b 		(a2),d1
				; Place un caractère nul juste après le nombre.
				clr.b 		(a2)
				; Lance la conversion
				; (avec l'adresse de départ comme paramètre dans A0).
				movea.l 	a1,a0
				jsr 		Convert
				; Si la conversion est valide,
				; D0 contient la valeur numérique du nombre ASCII.
				; On quitte sans erreur.
				beq 		\true
\false 			; Sortie avec erreur.
				; D0 n'a pas été modifié.
				; A0 contient l'adresse de départ de la chaîne.
				; Il ne reste plus qu'à restaurer le caractère sauvegardé dans D1.
				move.b 		d1,(a2)
				; Et renvoyer Z = 0.
				andi.b 		#%11111011,ccr
				bra 		\quit
\true 			; Sortie sans erreur.
				; On commence par restaurer le caractère sauvegardé dans D1.
				move.b 		d1,(a2)
				; On place l'adresse située après le nombre dans A0.
				movea.l 	a2,a0
				; Et enfin, on renvoie Z = 1.
				ori.b 		#%00000100,ccr
\quit 			; Restaure les registres.
				movem.l 	(a7)+,d1/a1-a2
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
				
	

