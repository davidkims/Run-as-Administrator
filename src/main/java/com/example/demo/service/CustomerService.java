package com.example.demo.service;
import com.example.demo.model.Customer;
import com.example.demo.repository.CustomerRepository;
import org.springframework.stereotype.Service;
import java.util.List;
@Service
public class CustomerService {
  private final CustomerRepository repo;
  public CustomerService(CustomerRepository repo){ this.repo=repo; }
  public Customer create(Customer c){
    if(repo.existsByEmail(c.getEmail()))
      throw new IllegalArgumentException("이미 존재하는 이메일입니다.");
    return repo.save(c);
  }
  public List<Customer> findAll(){ return repo.findAll(); }
}
