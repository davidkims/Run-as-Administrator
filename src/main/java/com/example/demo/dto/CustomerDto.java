package com.example.demo.dto;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
public class CustomerDto {
  @NotBlank @Size(max=100) private String name;
  @NotBlank @Email @Size(max=255) private String email;
  @Size(max=20) private String phone;
  public CustomerDto() {}
  public CustomerDto(String name,String email,String phone){ this.name=name; this.email=email; this.phone=phone; }
  public String getName(){return name;} public void setName(String v){this.name=v;}
  public String getEmail(){return email;} public void setEmail(String v){this.email=v;}
  public String getPhone(){return phone;} public void setPhone(String v){this.phone=v;}
}
