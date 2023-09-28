			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		movea.l	#String1,a0
			jsr		LowerCount
			

LowerCount	move.l	a0,-(a7)
			clr.l	d0
			
\loop		tst.b	(a0)+
			beq		\quit
			cmpi.b	#'a',(a0)
			blo		\loop
			cmpi.b	#'z',(a0)
			bhi		\loop
			addq.l	#1,d0
			bra		\loop
			

\quit		move.l	(a7)+,a0
			illegal
			
String1		dc.b	"Cette chaine comporte 28 minuscules.",0
