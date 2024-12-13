interface Shape{
    void getArea();
}
class Circle  implements Shape {
    int r;
    public Circle(int r){
        this.r = r;
    }
    public void getArea(){
        System.out.println(3.14*r*r);
    }
}
public class getA{
    public static void main(String[] args) {
        Circle c = new Circle(5);
        c.getArea();
    }
}