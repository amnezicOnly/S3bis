			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		movea.l	#String1,a0
			jsr		SpaceCount
			
			movea.l	#String2,a0
			jsr		SpaceCount
			
			illegal
			
SpaceCount	movem.l	a0/d1,-(a7)
			
			clr.l	d0
			
\loop		move.b	(a0)+,d1
			tst.b	d1
			beq		\quit
			cmp.b	#' ',(a0)
			bne		\loop
			addq.l	#1,d0
			bra		\loop
			
\quit		movem.l	(a7)+,d1/a0
			rts


String1		dc.b	"Cette chaine comporte 4 espaces.",0
String2     dc.b    "Celle-ci en comporte 3.",0
