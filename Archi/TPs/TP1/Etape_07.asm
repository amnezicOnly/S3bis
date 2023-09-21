			org		$4
Vector_001	dc.l	Main
			org		$500
			
Main		move.l	#$76543210,d1
			;move.l	d1,d2
			;move.l	d1,d3
			move.l	d1,d4
			
			
			;ror.w	#4,d2
			;rol.b	#4,d2
			;rol.w	#4,d2
			
			;rol.b	#4,d3
			;rol.w	#8,d3
			;rol.w	#4,d3
			;rol.b	#4,d3
			;rol.w	#8,d3
			;swap.w	d3
			;ror.w	#8,d3
			;rol.b	#4,d3
			;rol.w	#4,d3
			;ror.w	#8,d3
			;ror.b	#4,d3
			;swap.w	d3
			
			
			
