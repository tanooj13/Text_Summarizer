import java.util.*;
class Eve implements Runnable{
    int a;
    Eve(int a){
        this.a = a;
    }
    public void run(){
        System.out.println("Even");
    }

}
class Od implements Runnable{
    int a;
    Od(int a){
        this.a = a;
    }
    public void run(){
        System.out.println("Odd");
    }

}
class GenRandom extends Thread{

    public void run(){
        Random r = new Random();
        int n;
        try{
            for (int i = 0; i < 5; i++) {
                n = r.nextInt(20);
                System.out.println("Gen num: "+n);
                if (n%2 == 0){
                    Thread t2 = new Thread(new Eve(n));
                    t2.start();
                }else{
                    Thread t3 = new Thread(new Od(n));
                    t3.start();
                }
                Thread.sleep(1000);
            }
        }catch(Exception e){
            System.out.println(e);
        }
    }

}
public class RandomProb {
    public static void main(String[] args) {
        GenRandom r = new GenRandom();
        r.start();
    }
}