#include <stdio.h>

typedef struct {
    char estado[3];
    char codigo[8];
    char cidade[64];
    long long populacao;
    double area;
    double pib;
    int pontos;
} Carta;

double densidade(const Carta* c){ return (c->area>0)?((double)c->populacao/c->area):0.0; }
void limpa(){ int ch; while((ch=getchar())!='\n' && ch!=EOF){} }

void ler(Carta* c,const char* t){
    printf("\n=== Carta %s ===\n", t);
    printf("UF: "); scanf("%2s",c->estado); limpa();
    printf("Código: "); scanf("%7s",c->codigo); limpa();
    printf("Cidade: "); scanf("%63s",c->cidade); limpa();
    printf("População: "); scanf("%lld",&c->populacao); limpa();
    printf("Área: "); scanf("%lf",&c->area); limpa();
    printf("PIB: "); scanf("%lf",&c->pib); limpa();
    printf("Pontos: "); scanf("%d",&c->pontos); limpa();
}

int vencedor_por(int a,const Carta* A,const Carta* B){
    switch(a){
        case 1: return (A->populacao==B->populacao)?0:(A->populacao>B->populacao?-1:1);
        case 2: return (A->area==B->area)?0:(A->area>B->area?-1:1);
        case 3: return (A->pib==B->pib)?0:(A->pib>B->pib?-1:1);
        case 4: return (A->pontos==B->pontos)?0:(A->pontos>B->pontos?-1:1);
        case 5: {double dA=densidade(A),dB=densidade(B); return (dA==dB)?0:(dA<dB?-1:1);} 
    }
    return 0;
}

int main(){
    Carta A,B; int op;
    ler(&A,"A"); ler(&B,"B");
    printf("\nEscolha atributo (1=Pop,2=Área,3=PIB,4=Pontos,5=Densidade): ");
    scanf("%d",&op); limpa();
    int v=vencedor_por(op,&A,&B);
    if(v==0) printf("Empate!\n");
    else if(v==-1) printf("Vencedora: A (%s)\n",A.cidade);
    else printf("Vencedora: B (%s)\n",B.cidade);
    return 0;
}
