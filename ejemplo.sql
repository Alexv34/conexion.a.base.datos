PGDMP                          z            ejemplo    14.4    14.4     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16397    ejemplo    DATABASE     g   CREATE DATABASE ejemplo WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE ejemplo;
                postgres    false            ?            1259    16399    datos    TABLE     ?   CREATE TABLE public.datos (
    iddato integer NOT NULL,
    nombre character varying(30) NOT NULL,
    descripcion character varying(260),
    fecha date
);
    DROP TABLE public.datos;
       public         heap    postgres    false            ?            1259    16398    datos_iddato_seq    SEQUENCE     ?   CREATE SEQUENCE public.datos_iddato_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.datos_iddato_seq;
       public          postgres    false    210            ?           0    0    datos_iddato_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.datos_iddato_seq OWNED BY public.datos.iddato;
          public          postgres    false    209            \           2604    16402    datos iddato    DEFAULT     l   ALTER TABLE ONLY public.datos ALTER COLUMN iddato SET DEFAULT nextval('public.datos_iddato_seq'::regclass);
 ;   ALTER TABLE public.datos ALTER COLUMN iddato DROP DEFAULT;
       public          postgres    false    210    209    210            ?          0    16399    datos 
   TABLE DATA           C   COPY public.datos (iddato, nombre, descripcion, fecha) FROM stdin;
    public          postgres    false    210   ?       ?           0    0    datos_iddato_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.datos_iddato_seq', 11, true);
          public          postgres    false    209            ^           2606    16406    datos datos_nombre_key 
   CONSTRAINT     S   ALTER TABLE ONLY public.datos
    ADD CONSTRAINT datos_nombre_key UNIQUE (nombre);
 @   ALTER TABLE ONLY public.datos DROP CONSTRAINT datos_nombre_key;
       public            postgres    false    210            `           2606    16404    datos datos_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.datos
    ADD CONSTRAINT datos_pkey PRIMARY KEY (iddato);
 :   ALTER TABLE ONLY public.datos DROP CONSTRAINT datos_pkey;
       public            postgres    false    210            ?   ?   x?=?K
1?u{?^@?>@׮??M?)??;??g?bV??,?/???\hI?!??f???;s%??&t??%+?͐?,???>o??^??????%?gO?	_=?7?e??H$???^??O?h???yaW?m>???_d??0     