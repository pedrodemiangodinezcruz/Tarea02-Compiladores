.data
	newline:	.asciiz "\n"
	a:	.word 333
.text
	li $v0,1
	li $a0,333
	syscall 
	li $v0,4
	la $a0,newline
	syscall 
