package com.basic.array;

public class OneDimensionalArray {
    public static void main(String[] args) {
        //一维数组的声明与初始化
        int[] array1 = new int[5];//创建数组第一种方式,此时默认值都是为0
        array1[0] = 1;//数组名[索引] = 数值，为数组中的元素赋值
        array1[1] = 2;
        array1[2] = 3;

        int[] array2 = new int[]{1,2,3,4};//第二种方式：创建并初始化数组

        int[] array3 = {1,2,3,4};//第三种方式：创建并初始化数组

        //数组的长度属性length
        System.out.println("数组1的长度为："+ array1.length);
        //变量 = 数组名[索引]，获取出数组中的元素
        System.out.println("数组1的第二个元素为☞ "+ array1[1]);

        System.out.println("------数组遍历------");
        //数组遍历
        //1.for循环遍历方式
        for(int i=0;i<array2.length;i++){
            System.out.println(array2[i]);
        }

        System.out.println("-------------------");
        //2.foreach遍历方式
        for(int i: array2){
            System.out.println(i);
        }


        System.out.println("------数组反转------");
        /*
        * 实现反转，就需要将数组对称元素位置交换
        * 定义两个变量，保存数组的最小索引和最大索引
        * 两个索引上的元素交换位置 最小索引++，最大索引--，再次交换位置
        * 最小索引超过了最大索引，数组反转操作结束
         * */
        for(int min=0, max=array3.length-1;min<max;min++,max--){
            int temp = array3[min];
            array3[min] = array3[max];
            array3[max] = temp;
        }
        for (int i=0;i< array3.length;i++){
            System.out.println(array3[i]);
        }

        System.out.println("------数组获取最大元素------");
        /*
        *定义变量 max，保存数组0索引上的元素
        *遍历数组，获取出数组中的每个元素
        *将遍历到的元素和保存数组0索引上值的max变量进行比较
        *如果数组元素的值大于了变量的值，变量记录住新的值
        * 数组循环遍历结束，变量保存的就是数组中的最大值
        * */
        int max = array3[0];
        for (int i=0;i< array3.length;i++){
            if(max<array3[i]){
                max=array3[i];
            }
        }
        System.out.println(max);
    }
}
