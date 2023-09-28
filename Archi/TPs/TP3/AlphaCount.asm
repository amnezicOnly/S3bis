			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		movea.l	#String1,a0
			jsr		AlphaCount
			illegal
			
LowerCount	movem.l	a0,-(a7)
			clr.l	d0
			
\loop		tst.b	(a0)+
			beq		\quit
			cmpi.b	#'a',(a0)
			blo		\loop
			cmpi.b	#'z',(a0)
			bhi		\loop
			addq.l	#1,d0
			bra		\loop
			

\quit		add.l	d0,d1
			movem.l	(a7)+,a0
			rts
			
UpperCount	movem.l	a0,-(a7)
			clr.l	d0
			
\loop		tst.b	(a0)+
			beq		\quit
			cmpi.b	#'A',(a0)
			blo		\loop
			cmpi.b	#'Z',(a0)
			bhi		\loop
			addq.l	#1,d0
			bra		\loop
			

\quit		add.l	d0,d1
			movem.l	(a7)+,a0
			rts
			
DigitCount	movem.l	a0,-(a7)
			clr.l	d0
			
\loop		tst.b	(a0)+
			beq		\quit
			cmpi.b	#'0',(a0)
			blo		\loop
			cmpi.b	#'9',(a0)
			bhi		\loop
			addq.l	#1,d0
			bra		\loop
			

\quit		add.l	d0,d1
			movem.l	(a7)+,a0
			rts
			
AlphaCount	move.l	d1,-(a7)
			clr.l	d1
			jsr		LowerCount
			jsr		UpperCount
			jsr		DigitCount
			rts
			



String1		dc.b	"Cette chaine comporte 46 caracteres alphanumeriques.",0
