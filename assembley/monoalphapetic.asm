;encrypt a given text and decrypt it again
include 'emu8086.inc'

org 100h

JMP main
;DB to allocate data byte  
;Array_Name   Data_Type   Number_Of_Index   DUP(?)

;list1: abcdefghijklmnopqrstuvwxyz  

;list2: qwertyuiopasdfghjklzxcvbnm  

;list3: kxvmcnophqrszyijadlegwbuft 
 
;abc -->qwe is compared from list1 with list 2
;qwe -->abc is compared from list1 with list 3  

table1      DB 97 dup ('$'), 'kxvmcnophqrszyijadlegwbuft'

table2      DB 97 dup ('$'), 'qwertyuiopasdfghjklzxcvbnm'

msg1        DB  'Enter the message: ', '$'    ;const string decleration

msg2        DB  'Encrypted message: ', '$'

msg3        DB  'Decrypted message: ', '$' 

;256 DUP('$') to fill all the 256 with $ instead of garbage 

n_line      DB  0DH,0AH,'$'                 ;for new line

MESSAGE     DB  256 DUP('$')                ;buffer string

ENCRYPTED   DB  256 DUP('$')                ;encrypted string

DECRYPTED   DB  256 DUP('$')                ;decrypted string


 

main:            
; print message  
LEA    DX,msg1
; output of a string at ds:dx
MOV    AH,09h
INT    21h ; int21 used to interact with cmd



;to set your data segment to the same value as your code segment.
;Hence cs and ds should be set to the same value so that all instructions operated on that segment by default.
PUSH   CS
POP    DS 


; read the string
LEA    DI,MESSAGE
MOV    DX,00FFH
CALL   GET_STRING
; print new line 
LEA    DX,n_line
; output of a string at ds:dx
MOV    AH,09h
INT    21h                
                                 
; encrypt:
LEA    BX, table2 ;base address now hold start address of table1
LEA    SI, MESSAGE ;source
LEA    DI, ENCRYPTED;destination
CALL   CRYPT ;same function do both but we change the base address before the call
                                          
; print message
LEA    dx,msg2
; output of a string at ds:dx
MOV    ah,09h
INT    21h
; show result:
LEA    dx, ENCRYPTED
; output of a string at ds:dx
MOV    ah, 09
INT    21h
; print new line
LEA    dx,n_line
; output of a string at ds:dx
MOV    ah,09h
INT    21h     
 
          
; decrypt:
LEA    bx, table1
LEA    si, ENCRYPTED  ;need to decrypt this 
LEA    di, DECRYPTED  ;destination
CALL   CRYPT   

; print message
LEA    dx,msg3
; output of a string at ds:dx
MOV    ah,09h
INT    21h
; show result:
LEA    dx, DECRYPTED
; output of a string at ds:dx
MOV    ah, 09
INT    21h
; print new line
LEA    dx,n_line
; output of a string at ds:dx
MOV    ah,09h
INT    21h

;2 lines ends the program                
MOV    AH, 0
INT    16h          
    


CRYPT proc near   ; procedure 

next_char:
	
    cmp    [si], '$'      ; end of string?
	je     end_of_string
	cmp    [si], ' '      ;find a space ?
	je     skip
;ja :if (CF = 0) and (ZF = 0) then jump
;jb :if CF=1
;je :if ZF = 1 then jump
	
	mov    al, [si]  ; each time till hit end [si] --> AL
	;any letter - 'a' >= 0 except for the upper case letters
    ;our program will skip upper letters
    cmp    al, 'a'   
	jb     skip  
    ; any letter - 'z' will result a CF=1 except 'z' will result CF=0 and ZF=1 
    ; doesn't satisfy ja conditions
    ;will satisfy if only not in range 97:122 so it wil skip it 
	cmp    al, 'z'
	ja     skip	
    

    ; xlat algorithm: al = ds:[bx + unsigned al] 
	xlatb      
	mov    [di], al
	inc    di

skip:
	inc    si	 ;increment by 1
	jmp    next_char ;return to the procedure


end_of_string:   ;add the terminator
    inc    si
    mov    [si], '$'

ret   ; return from procedure
CRYPT endp
     

DEFINE_GET_STRING       ;predefined macro in "emu8086.inc" reads a string input
END
