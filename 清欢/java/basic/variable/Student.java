package com.basic.variable;

public class Student {
    int age;//成员变量
    public static String status = "student";//类变量
    public void study(){
        String achievement = "s";//局部变量
        System.out.println("--- sheer hard work--");
    }

    public static void main(String[] args) {
        Subject subject1 = new Subject("math");
        subject1.join();
        Subject.count++;
        Subject subject2 = new Subject("Chinese");
        subject2.join();
        Subject.count++;
        System.out.println(subject1.count+"门课的成绩很好");

    }
}
class Subject{
    private String name;//成员变量
    public static int count = 0;//类变量
    public Subject(String name){
        this.name=name;
    }
    public void join(){
        int scoure = 99;//局部变量
        System.out.println( "She earned her grades through "+ name + ",scoure is "+scoure );
    }
}
