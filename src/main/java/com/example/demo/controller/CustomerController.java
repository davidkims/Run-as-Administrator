package com.example.demo.controller;
import com.example.demo.dto.CustomerDto;
import com.example.demo.mapper.CustomerMapper;
import com.example.demo.model.Customer;
import com.example.demo.service.CustomerService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;
@RestController
@RequestMapping("/customers")
@Tag(name="Customers", description="Customer CRUD API")
public class CustomerController {
  private final CustomerService svc;
  private final CustomerMapper mapper;
  public CustomerController(CustomerService svc, CustomerMapper mapper){
    this.svc=svc; this.mapper=mapper;
  }
  @PostMapping
  @Operation(summary="Create customer")
  public ResponseEntity<Customer> create(@Valid @RequestBody CustomerDto dto){
    Customer saved = svc.create(mapper.toEntity(dto));
    return ResponseEntity.ok(saved);
  }
  @GetMapping
  @Operation(summary="List customers")
  public ResponseEntity<List<Customer>> list(){
    return ResponseEntity.ok(svc.findAll());
  }
}
