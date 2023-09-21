			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		move.w	NUMBER1,d0
			add.w	NUMBER2,d0
			move.w	d0,SUM			; utilité de cette ligne ???
			
			illegal
			
			org		$550
			
NUMBER1		dc.w	$2222
NUMBER2		dc.w	$5555
SUM			ds.w	1
