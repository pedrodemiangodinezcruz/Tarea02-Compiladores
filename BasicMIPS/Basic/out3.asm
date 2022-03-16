.data
	newline:	.asciiz "\n"
	a:	.word 555
.text
	li $v0,1
	li $a0,666
	syscall 
	li $v0,4
	la $a0,newline
	syscall 
