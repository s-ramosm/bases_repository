/*==============================================================*/
/* Table: "Candidato"                                           */
/*==============================================================*/
create table "Candidato" (
   "Usuario"            VARCHAR2(30)          not null,
   "Id Tipo de Documento" VARCHAR2(3)           not null,
   "Nombre"             VARCHAR2(30)          not null,
   "Apellido"           VARCHAR2(30)          not null,
   "Fecha de Nacimiento" DATE                  not null,
   "Número de Documento" NUMBER(15)            not null,
   constraint PK_CANDIDATO primary key ("Usuario")
);

/*==============================================================*/
/* Index: "En_FK"                                               */
/*==============================================================*/
create index "En_FK" on "Candidato" (
   "Id Tipo de Documento" ASC
);

/*==============================================================*/
/* Table: "Tipo de Documento"                                   */
/*==============================================================*/
create table "Tipo de Documento" (
   "Id Tipo de Documento" VARCHAR2(3)           not null,
   "Tipo de Documento"  VARCHAR2(20)          not null,
   constraint "PK_TIPO DE DOCUMENTO" primary key ("Id Tipo de Documento")
);

alter table "Candidato"
   add constraint "FK_CANDIDAT_EN_TIPO DE" foreign key ("Id Tipo de Documento")
      references "Tipo de Documento" ("Id Tipo de Documento");

