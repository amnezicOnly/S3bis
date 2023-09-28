			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		movea.l	#String1,a0
			jsr		Atoui
			illegal
			
Atoui		movem.l	a0/d1,-(a7)
			move.l	#0,d1
			
\loop		move.b	(a0)+,d1
			tst.b	d1
			beq		\quit
			subi.w	#'0',d1
			mulu.w	#10,d0
			add.w	d1,d0
			bra		\loop
			
\quit		movem.l	(a7)+,d1/a0
			rts

String1 	dc.b	"1234",0
