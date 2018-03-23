clc
clear all
close all

Feldgroese = 100;
Feld2=zeros(Feldgroese,Feldgroese);
Futterposition1 = 60;
Futterposition2 = 90;
Futter=[Futterposition1;Futterposition2];
Startpunkt1=10;
Startpunkt2=10;
Feld = zeros(Feldgroese,Feldgroese);
Feld(Futterposition1,Futterposition2)=Feldgroese;


for i=1:Feldgroese
    for j = 1:Feldgroese
    d=sqrt((i-Futterposition1)^2+(j-Futterposition2)^2);
    Feld(i,j)=Feldgroese-d;
    end
end

imagesc(Feld)
hold on

Kopf=zeros(2,1);
Brust=zeros(2,1);
Arsch=zeros(2,1);
Schwanz=zeros(2,1);
Start=[Startpunkt1;Startpunkt2];

Kopf=Start;
Brust=[Startpunkt1+1;Startpunkt2];
Arsch=[Startpunkt1+2;Startpunkt2];
Schwanz=[Startpunkt1+3;Startpunkt2];

Richtungen=[0,1;-1,0;1,0;0,-1];
r = randi(4,1,1);
Richtung=Richtungen(r,:);
Richtung=(Richtung)';

while Feld(Kopf(1),Kopf(2)) <Feldgroese
 
while Feld(Kopf(1),Kopf(2)) <= Feldgroese*0.5
    r = randi(4,1,1);
    Richtung=Richtungen(r,:);
    Richtung=(Richtung)';
    Kopf_neu=Kopf+Richtung;
    while Kopf_neu==Brust | Kopf_neu(1,1)==100 | Kopf_neu(2,1)==100 | Kopf_neu(1,1)==0 | Kopf_neu(2,1)==0
        r = randi(4,1,1);
        Richtung=Richtungen(r,:);
        Richtung=(Richtung)';
        Kopf_neu=Kopf+Richtung;  
    end
    Schwanz=Arsch;
    Arsch=Brust;
    Brust=Kopf;
    Kopf=Kopf_neu;
    Feld2(Kopf_neu(1,1),Kopf_neu(2,1))=Feldgroese;
end

while Feld(Kopf(1),Kopf(2)) > Feldgroese*0.5
    if Kopf == Futter
    fprintf('omnomnom!!!!!!!!')
    break
    else
    r = randi(4,1,1);
    Richtung=Richtungen(r,:);
    Richtung=(Richtung)';
    Kopf_neu=Kopf+Richtung;
    if Feld(Kopf(1),Kopf(2))<Feld(Kopf_neu(1),Kopf_neu(2));
       Schwanz=Arsch;
       Arsch=Brust;
       Brust=Kopf;
       Kopf=Kopf_neu;
       Feld2(Kopf_neu(1,1),Kopf_neu(2,1))=Feldgroese;
    else
    r = rand;
    if r<0.4
       Schwanz=Arsch;
       Arsch=Brust;
       Brust=Kopf;
       Kopf=Kopf_neu;
       Feld2(Kopf_neu(1,1),Kopf_neu(2,1))=Feldgroese;
    else
        r = randi(4,1,1);
        Richtung=Richtungen(r,:);
        Richtung=(Richtung)';
        Kopf_neu=Kopf+Richtung;
        while Kopf_neu==Brust | Kopf_neu(1,1)==100 | Kopf_neu(2,1)==100 | Kopf_neu(1,1)==0 | Kopf_neu(2,1)==0
            r = randi(4,1,1);
            Richtung=Richtungen(r,:);
            Richtung=(Richtung)';
            Kopf_neu=Kopf+Richtung;  
         end
    end
    end
    end
end
end

imagesc(Feld2)
hold off
alpha 0.5
axis off 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        