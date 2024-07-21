create table users(
    id integer primary key,
    name text not null,
    passwd text null,
    sec_tip text,
    sec_ans text
);

create table accounts(
    id integer primary key,
    user_id integer not null,
    currency text not null default 'AUD',
    name text not null,
    note text null,
    balance integer default 0,
    unique(user_id, currency)
);