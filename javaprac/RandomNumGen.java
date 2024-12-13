import java.util.*;
class Even implements Runnable{
    int a;
    Even(int a){
        this.a = a;
    }
    public void run(){
        System.out.println("Even num"+a+" square is :"+(a*a));
    }
}
class Odd implements  Runnable{
    int a;
    public Odd(int a){
        this.a = a;
    }
    public void run(){
        System.out.println("Odd num "+a+"Cube:"+(a*a*a));
    }
}
class RandomGen extends Thread{

    public void run(){
        int n;
        Random r = new Random();
        try {
            for (int i = 0; i < 5; i++) {
                n = r.nextInt(20);
                System.out.println("gen num:" + n);
                if (n%2 == 0){
                    Thread t2 = new Thread(new Even(n));
                    t2.start();
                }else{
                    Thread t3 = new Thread(new Odd(n));
                    t3.start();
                }
                Thread.sleep(1000);
            }
        }catch(Exception e){
            System.out.println(e.getMessage());
        }
    }
}

public class RandomNumGen {
    public static void main(String[] args) {
        RandomGen ra = new RandomGen();
        ra.start();
    }
}