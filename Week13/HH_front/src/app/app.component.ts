import {Component, OnInit} from '@angular/core';
import {CompanyService} from "./company.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'servicesGroup2';

  logged = false;

  username = '';
  password = '';

  constructor(private companyService: CompanyService) {}

  ngOnInit(){
    let token = localStorage.getItem('token');
    if (token){
      this.logged = true;
    }
  }

  login(){
    this.companyService.login(this.username, this.password)
      .subscribe(res => {

        localStorage.setItem('token', res.token);

        this.logged = true;

        this.username = '';
        this.password = '';
      })
  }

  logout(){
    localStorage.clear();
    this.logged = false;
  }

}
