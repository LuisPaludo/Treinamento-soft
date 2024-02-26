import { Component, OnInit } from '@angular/core';
import { MessageService } from 'primeng/api';
import { GetAllProductsResponse } from 'src/app/models/products/response/GetAllProducts.response';
import { ProductsService } from 'src/app/services/products/products.service';
import { ProductsDataTransferService } from 'src/app/shared/services/products/products-data-transfer.service';

@Component({
  selector: 'app-dashboard-home',
  templateUrl: './dashboard-home.component.html',
  styleUrls: []
})
export class DashboardHomeComponent implements OnInit{

  public productsList: Array<GetAllProductsResponse> = [];

  constructor(
    private productsService: ProductsService,
    private messageService: MessageService,
    private productsDtService: ProductsDataTransferService,
  ) {}

  ngOnInit(): void {
    this.getProductsDatas();
  }

  getProductsDatas() {
    this.productsService.GetAllProducts().subscribe({
      next: (response) => {
        if (response.length > 0) {
          this.productsList = response;
          this.productsDtService.setProductsDatas(this.productsList);
        }
      },
      error: (err) => {
        this.messageService.add({
          severity: 'error',
          summary: 'Erro',
          detail: 'Erro ao buscar produtos!',
          life: 2500,
        })
      }
    })
  }

}
