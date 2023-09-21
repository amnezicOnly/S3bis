			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		move.l	#$1,d0
			move.l	#1,d1
			move.l	#2,d2
			move.l	#3,d3
			move.l	#$FFFFFFFF,d4
			move.l	#5,d5
			move.l	#6,d6
			move.l	#7,d7
			
			
			add.l	d4,d0
			addx.l	d5,d1
			addx.l	d6,d2
			addx.l	d7,d3
			illegal
