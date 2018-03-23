clc
clear all

Anfang=[0;0]

N1=0;
N2=0;
N3=0;
N4=0; 
SN3=1;
SN4=1;
 
w31=1.5;
w41=-1;
w32=1.5;
w42=-1;
w43=2.5;

if Anfang(1)==1
    N4=N4+w41;
    N3=N3+w31;
else
    fprintf('N1 inaktiv, ')
end

if Anfang(2)==1
     N4=N4+w42;
    N3=N3+w32;
else
    fprintf('N2 inaktiv, ')
end

if N3>=SN3
    N4=N4+w43;
else
    fprintf('N3 inaktiv, ')
end

if N4>=SN4
    fprintf('N4 aktiv, ')
else
    fprintf('N4 inaktiv, ')
end