import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
class AddressBookEntry {
    private String name;
    private String phone;
    private String email;
    public AddressBookEntry(String name, String phone, String email){
        this.name = name;
        this.phone = phone;
        this.email = email;
    }
    public String getName(){
        return name;
    }
    public String getPhone(){
        return phone;
    }
    public String getEmail(){
        return email;
    }
}
class AddressBook {
    private ArrayList <AddressBookEntry> list = new ArrayList<AddressBookEntry>();
    public void addNew(String name,String phone,String email){
        AddressBookEntry person = new AddressBookEntry(name,phone,email);
        list.add(person);
    }
    public void del(String name,String phone,String email){
        AddressBookEntry person = new AddressBookEntry(name,phone,email);
        list.remove(person);
    }
    public int find(String name,String phone,String email){
        AddressBookEntry person = new AddressBookEntry(name,phone,email);
        return list.indexOf(person);
    }
}

class AddressBookMain {
    public static String r() throws IOException{
        BufferedReader str = new BufferedReader(new InputStreamReader(System.in));
        String op = str.readLine();
        return op;
    }
    public static void main(String args []) throws IOException{
        AddressBook mainBook = new AddressBook();
        System.out.println("Please choose which operation:\n");
        System.out.println("1. add\n2.delete\n3.find\n");
        String op = r();
        String name,phone,email;
        switch(op) {
            case "add":
                System.out.println("Name:\n");
                name = r();
                System.out.println("phone:\n");
                phone = r();
                System.out.println("email:\n");
                email = r();
                mainBook.addNew(name,phone,email);
                break;
            case "delete":
                System.out.println("Name:\n");
                name = r();
                System.out.println("phone:\n");
                phone = r();
                System.out.println("email:\n");
                email = r();
                mainBook.del(name,phone,email);
                break;
            case "find" :
            System.out.println("Name:\n");
            name = r();
            System.out.println("phone:\n");
            phone = r();
            System.out.println("email:\n");
            email = r();
                mainBook.find(name,phone,email);
                break;
            default:
                System.out.println("wrong opertion");
        }

    }
}