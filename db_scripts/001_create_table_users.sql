create table users
(
    id      integer primary key,
    name    text not null,
    passwd  text null,
    sec_tip text,
    sec_ans text
);

create table accounts
(
    id      integer primary key,
    user_id integer not null,
--     currency text not null default 'AUD',
    name    text    not null,
    desc    text null,
    balance text null,
    unique (user_id, name)
);

create table options
(
    id        integer primary key,
    user_id   integer not null,
    type      text    not null,
    name      text    not null,
    parent_id integer default 0,
    desc      text null,
    unique (user_id, type, name)
);

create table expenses
(
    id          integer primary key,
    user_id     integer not null,
    evt_date    date    not null,
    account_id  integer not null,
    cat_id      integer not null,
    subcat_id   integer null,
    amount      REAL null,
    currency_id integer null,
    note        text null
);
create index exp_idx_user_id on expenses (user_id);