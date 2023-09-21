			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		move.l	#-65535,d0

Abs			neg.l	d0
			illegal
