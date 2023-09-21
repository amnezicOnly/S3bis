			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		movea.l	#STRING,a0


StrLen		tst.b	(a0)+
			beq		Quit
			cmpi.b	#'a',(a0)
			blt		StrLen
			cmpi.b	#'z',(a0)
			bgt		StrLen
			addq.l	#1,d0
			bra		StrLen

Quit		illegal		


STRING		dc.b	"Cette chaine comporte 28 minuscules.",0
