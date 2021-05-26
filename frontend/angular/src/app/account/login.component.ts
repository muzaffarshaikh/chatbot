import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormControl,FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';
import { RestService } from '../rest.service';
import { AccountService, AlertService } from '@app/_services';
import { MustMatch } from '@app/_helpers';

@Component({ 
    selector: 'app-root',
    templateUrl: 'login.component.html' 
})
export class LoginComponent implements OnInit {
    logform: FormGroup;
    loading = false;
    submitted = false;
    url_for : RestService;

    constructor(
        private readonly http: HttpClient,
        public rs: RestService,
        private formBuilder: FormBuilder,
        private route: ActivatedRoute,
        private router: Router,
        private accountService: AccountService,
        private alertService: AlertService
    ) 
        {this.logform = new FormGroup({ 
            'email': new FormControl('', [
              Validators.required
            ]),
            'password': new FormControl('', [
              Validators.required
            ])
          }); }
         
     

    ngOnInit() {
        this.logform = this.formBuilder.group({
            email: ['', [Validators.required, Validators.email]],
            password: ['', Validators.required]
        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.logform.controls; }

    public onSubmit():void  {
        console.log(this.logform.value); // printing the values(user input) in console
        var val=this.logform.value;
        this.http.post("http://localhost:5000/login_data/ ", val).subscribe((data) => {});

        this.submitted = true;

        // reset alerts on submit
        this.alertService.clear();

        // stop here if form is invalid
        if (this.logform.invalid) {
            return;
        }

        this.loading = true;
        this.accountService.login(this.f.email.value, this.f.password.value)
            .pipe(first())
            .subscribe({
                next: () => {
                    // get return url from query parameters or default to home page
                    const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
                    this.router.navigateByUrl(returnUrl);
                },
                error: error => {
                    this.alertService.error(error);
                    this.loading = false;
                }
            });
    }
}