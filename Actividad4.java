/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */
package com.mycompany.actividad4;

import java.util.Scanner;

/**
 *
 * @author Sala de Sistemas
 */
public class Actividad4 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int edad;
        String nombre;
        String apellido;
        int sexo;
        

        System.out.println("ingrese un nombre:");
        nombre = entrada.nextLine();
         System.out.println("ingrese el apellido:");
        apellido = entrada.nextLine();
        System.out.println("ingrese una edad:");
        edad = entrada.nextInt();
        System.out.println("eliga el sexo: hombre(1), mujer(2)");
        sexo = entrada.nextInt();
        
        

        if (edad >= 18) {
            System.out.println("es mayor de edad");
        } else {
            System.out.println("es menor de edad");
        }
        switch(sexo){
            case 1: 
                System.out.println("es un hombre");
                break;
            case 2:
                System.out.println("es una mujer");
                break; 
        }
      

    }

}
