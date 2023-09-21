			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		movea.l	#STRING,a0


StrLen		addq.l	#1,d0
			tst.b	(a0)+
			bne		StrLen
			subq.l	#1,d0
			illegal
			
			org		$550			


STRING		dc.b	"Cette chaine comporte 36 caracteres.",0
