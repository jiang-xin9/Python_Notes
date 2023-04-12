package com.basic.array;

import java.util.Arrays;

public class API {
    /*
     * java.util.Arrays:操作数组的工具类，里面定义了很多操作数组的方法
     *
     *
     */
    public static void output(int[] arr) {
        if(arr !=null){
            for(int i=0;i<arr.length;i++){
                System.out.println(arr[i] + " ");
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[5];

        // 填充数组
        Arrays.fill(arr,5);
        System.out.println("填充数组：Arrays.fill(array, 5)：");
        API.output(arr);

        // 将数组的第2和第3个元素赋值为8
        Arrays.fill(arr, 2, 4, 8);
        System.out.println("将数组的第2和第3个元素赋值为8：Arrays.fill(array, 2, 4, 8)：");
        API.output(arr);

        // 对整个数组进行排序
        int[] arr1 = { 7, 8, 3, 2, 12, 6, 3, 5, 4 };
        Arrays.sort(arr1);
        System.out.println("对整个数组进行排序：Arrays.sort(array1)：");
        API.output(arr1);

        // 比较数组元素是否相等
        System.out.println("比较数组元素是否相等:Arrays.equals(array, array1):" + "\n" + Arrays.equals(arr,arr1));
        int[] arr2 = arr1.clone();
        System.out.println("克隆后数组元素是否相等:Arrays.equals(array1, array2):" + "\n" + Arrays.equals(arr1, arr2));

        //输出数组 Arrays.toString()
        System.out.println("输出数组:Arrays.toString(arr1):" + "\n" +Arrays.toString(arr1));
    }
}
