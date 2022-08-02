public class insertSort {
    public static void sort(Comparable[] list){
        int len = list.length;
        for(int i =1;i<len;i++){
            for(int j=i;j>0;j--){
                if(list[j].compareTo(list[j-1]) < 0){
                    swap(list,j,j-1);
                }
                else{
                    break;
                }
            }
        }
    }
    private static void swap(Object [] list,int i,int j){
        Object temp = list[i];
        list[i] = list[j];
        list[j] = temp;
    }
    public static void main(String[] args){
        Integer[] list = {3,6,3,5,2,1,7};
        sort(list);
        for(int num:list){
            System.out.println(num);
        }
    }
}
