.data
	newline:	.asciiz "\n"
	x:	.word 4
.text
	li $v0,1
	li $a0,0
	syscall 
	li $v0,4
	la $a0,newline
	syscall 
	li $v0,1
	li $a0,0
	syscall 
	li $v0,4
	la $a0,newline
	syscall 
