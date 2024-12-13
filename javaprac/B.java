class A{
public void m1(){
System.out.println("Parent");
} 
}

public class B extends A{
public void m1(){
System.out.println("Child");

}
public static void main(String[] args){
A a = new A();
B b = new B();
A ab = new B();
a.m1();
b.m1();
ab.m1();
}
}