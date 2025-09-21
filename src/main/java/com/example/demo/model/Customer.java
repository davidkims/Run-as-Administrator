package com.example.demo.model;
import jakarta.persistence.*;
@Entity @Table(name = "customers")
public class Customer {
  @Id @GeneratedValue(strategy = GenerationType.IDENTITY) private Long id;
  @Column(nullable = false, length = 100) private String name;
  @Column(nullable = false, unique = true, length = 255) private String email;
  @Column(length = 20) private String phone;
  public Customer() {}
  public Customer(Long id, String name, String email, String phone) { this.id=id; this.name=name; this.email=email; this.phone=phone; }
  public Long getId(){return id;} public void setId(Long id){this.id=id;}
  public String getName(){return name;} public void setName(String n){this.name=n;}
  public String getEmail(){return email;} public void setEmail(String e){this.email=e;}
  public String getPhone(){return phone;} public void setPhone(String p){this.phone=p;}
}
