(define (reverse lst)
  (cond
    ((null? lst) ())
    ((null? (cdr lst)) lst)
    (else (append (reverse (cdr lst)) (list (car lst)))))
)

;(define (longest-increasing-subsequence lst)
;    (cond
;      ((null? lst) ())
;      ((null? (cdr lst)) lst)
;      ((< (car lst) (car (cdr lst))) (cons (car lst) (longest-increasing-subsequence (cdr lst))))
;      ((< (length (longest-increasing-subsequence (cons (car lst) (cdr (cdr lst)))))
;          (length (longest-increasing-subsequence (cdr lst))))
;        (longest-increasing-subsequence (cdr lst)))
;      (else (longest-increasing-subsequence (cons (car lst) (cdr (cdr lst)))))))

; helper fn
(define (larger-vals x lst) (filter (lambda (v) (> v x)) lst))

;(define (longest-increasing-subsequence lst)
;  (cond
;      ((null? lst) ())
;      ((null? (cdr lst)) lst)
;      ((> (length (larger-vals (car lst) (cdr lst)))
;          (length (larger-vals (car (cdr lst)) (cdr (cdr lst)))))
;        (longest-increasing-subsequence (cons (car lst) (larger-vals (car lst) (cdr lst)))))
;      (else (longest-increasing-subsequence (cons (car lst) (larger-vals (car (cdr lst)) (cdr (cdr lst))))))))

(define (longest-increasing-subsequence lst)
  (if (null? lst)
      nil
      (begin
        (define first (car lst))
        (define rest (cdr lst))
        (define large-vals-rest
                (larger-vals first rest))
        (define with-first
                (cons
                  (car lst)
                  (longest-increasing-subsequence large-vals-rest)))
        (define without-first
                (longest-increasing-subsequence rest))
        (if (> (length with-first) (length without-first))
            with-first
            without-first))))


(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))


; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (make-sum (derive (addend expr) var)
            (derive (augend expr) var)
  )
)

; TODO on derive product!!

(define (derive-product expr var)
  (make-sum (make-product (derive (multiplier expr) var)
                          (multiplicand expr))
            (make-product (multiplier expr)
                          (derive (multiplicand expr) var))))

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond ((=number? exponent 0) 1)
        ((=number? exponent 1) base)
        ((and (number? base)(number? exponent)) (expt base exponent))
        (else (list '^ base exponent))
  )
)

(define (base exp)
  (car (cdr exp))
)

(define (exponent exp)
  (car (cdr (cdr exp)))
)

(define (exp? exp)
  (cond ((number? exp) #f)
        ((variable? exp) #f)
        ((number? (car exp)) #f)
        ((equal? (car exp) '^) #t)
        (else #f)
))

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  (cond ((= (exponent exp) 2) (list '* 2 var))
        (else (list '* (exponent exp)
                    (list '^ var (- (exponent exp) 1))))))