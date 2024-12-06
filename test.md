```
[64]
SHR AX
* Shifts right AX by one bit. [Effectively dividing by 2]
ALUx<-[AX]
ALUr=[ALUx]>>1
AX<-[ALUr]

[65]
SHR BX
* Shifts right BX by one bit. [Effectively dividing by 2]
ALUx<-[BX]
ALUr=[ALUx]>>1
BX<-[ALUr]