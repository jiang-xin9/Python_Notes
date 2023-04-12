package com.basic.array;

public class ArrayException {
    /*
     * 数组中的常见异常：
     * 1. 数组角标越界的异常：ArrayIndexOutOfBoundsExcetion
     *
     * 2. 空指针异常：NullPointerException
     *
     */
    public static void main(String[] args) {
        //数组越界异常
        int[] array = new int[]{1,2,3,3,3,3};
//        System.out.println(array[111]);


        //数组空指针异常
        array=null;
        System.out.println(array[1]);
    }
}
