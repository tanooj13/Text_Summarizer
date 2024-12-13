abstract class Marks{
    abstract void getPercentage();

}

class StudentA extends Marks{
    int a,b;

    StudentA(int a,int b){
        this.a = a;
        this.b = b;

    }
    void getPercentage(){
        System.out.println("A " +(a+b)/2);
    }

}
class StudentB extends Marks{
    int a,b,c;

    StudentB(int a,int b,int c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
    void getPercentage(){
        System.out.println("B " +(a+b+c)/3);
    }

}
public class Cal {
    public static void main(String[] args) {
        StudentA a = new StudentA(100,100);
        StudentB b = new StudentB(99,98,97);
        a.getPercentage();
        b.getPercentage();
    }

}