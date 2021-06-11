import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

enum EmailStatus {
    Verifying,
    Failed
}

@Component({ templateUrl: 'verify-email.component.html' })
export class VerifyEmailComponent implements OnInit {
    EmailStatus = EmailStatus;
    emailStatus = EmailStatus.Verifying;

    constructor(
        private route: ActivatedRoute
    ) { }

    ngOnInit() {
        const token = this.route.snapshot.queryParams['token'];
    }
}