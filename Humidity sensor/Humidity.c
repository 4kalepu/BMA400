#include<stdio.h>
#include<string.h>
int main(){

   int i,j,k,l,m,n;
    int dth[40],temp[16],hum[16],crc[8];
    for(i=0;i<16;i++){
        for ( j =16 ; j<31; j++)
        {
            temp[i]=dth[j];
        }
        
    }
    for(n=0;n<8;n++){
        for ( m =32 ; m<40; m++)
        {
            crc[i]=dth[j];
        }
        
    }
    for(k=0;k<16;i++){
        for (l=0; l<16; l++)
        {
            hum[i]=dth[j];
        }
        
    }
 
 int tlen=str(temp);
 int hlen=str(hum);

for(int f=(tlen-1);f>=4;f--)
{
    int Ftemp = Ftemp + (pow(2,i) * (temp[f] - '0'));
    f++;
}
for(int g=(hlen-1);g>=4;g--)
{
    int Fhum = Fhum + (pow(2,i) * (hum[g] - '0'));
    g++;
}






  

}