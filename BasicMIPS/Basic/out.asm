.data
	newline:	.asciiz "\n"
	a:	.word 5
	b:	.word 6
	c:
.text
	li $v0,1
	li $a0,193
	syscall 
	li $v0,4
	la $a0,newline
	syscall 
	li $t1,6
	li $t2,2
	mul $t0,$t1,$t2
	li $t1,5
	li $t2,12
	addu $t0,$t1,$t2
	la $a0,c
	move $a1,$t0
	sw $a1,0($a0)
	li $v0,1
	li $a0,17
	syscall 
	li $v0,4
	la $a0,newline
	syscall 
	li $t1,1
	li $t2,2
	addu $t0,$t1,$t2
	li $t1,3
	li $t2,3
	mul $t0,$t1,$t2
	li $v0,1
	li $a0,9
	syscall 
	li $v0,4
	la $a0,newline
	syscall 
