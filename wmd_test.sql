--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Artist; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Artist" (
    id integer NOT NULL,
    name character varying,
    image_link character varying(500)
);


ALTER TABLE public."Artist" OWNER TO postgres;

--
-- Name: Artist_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Artist_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Artist_id_seq" OWNER TO postgres;

--
-- Name: Artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Artist_id_seq" OWNED BY public."Artist".id;


--
-- Name: Record; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Record" (
    id integer NOT NULL,
    name character varying,
    isbn character varying,
    artist_id integer,
    image_link character varying(500)
);


ALTER TABLE public."Record" OWNER TO postgres;

--
-- Name: Record_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Record_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Record_id_seq" OWNER TO postgres;

--
-- Name: Record_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Record_id_seq" OWNED BY public."Record".id;


--
-- Name: Artist id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist" ALTER COLUMN id SET DEFAULT nextval('public."Artist_id_seq"'::regclass);


--
-- Name: Record id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Record" ALTER COLUMN id SET DEFAULT nextval('public."Record_id_seq"'::regclass);


--
-- Data for Name: Artist; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Artist" (id, name, image_link) FROM stdin;
1	Artist 1	http://www.website.com/artist/1
2	Artist 2	http://www.website.com/artist/2
3	Artist 3	http://www.website.com/artist/3
4	Artist 4	http://www.website.com/artist/4
5	Artist 5	http://www.website.com/artist/5
6	Artist 6	http://www.website.com/artist/6
7	Artist 7	http://www.website.com/artist/7
8	Artist 8	http://www.website.com/artist/8
9	Artist 9	http://www.website.com/artist/9
10	Artist 10	http://www.website.com/artist/10
11	Artist 11	http://www.website.com/artist/11
12	Artist 12	http://www.website.com/artist/12
13	Artist 13	http://www.website.com/artist/13
14	Artist 14	http://www.website.com/artist/14
15	Artist 15	http://www.website.com/artist/15
16	Artist 16	http://www.website.com/artist/16
17	Artist 17	http://www.website.com/artist/17
18	Artist 18	http://www.website.com/artist/18
19	Artist 19	http://www.website.com/artist/19
20	Artist 20	http://www.website.com/artist/20
21	Artist 21	http://www.website.com/artist/21
22	Artist 22	http://www.website.com/artist/22
23	Artist 23	http://www.website.com/artist/23
24	Artist 24	http://www.website.com/artist/24
25	Artist 25	http://www.website.com/artist/25
26	Artist 26	http://www.website.com/artist/26
27	Artist 27	http://www.website.com/artist/27
28	Artist 28	http://www.website.com/artist/28
29	Artist 29	http://www.website.com/artist/29
\.


--
-- Data for Name: Record; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Record" (id, name, isbn, artist_id, image_link) FROM stdin;
1	Record 1	666666	1	http://www.website.com/record/1
2	Record 2	666667	2	http://www.website.com/record/2
3	Record 3	666668	3	http://www.website.com/record/3
4	Record 4	666669	4	http://www.website.com/record/4
5	Record 5	666670	5	http://www.website.com/record/5
6	Record 6	666671	6	http://www.website.com/record/6
7	Record 7	666672	7	http://www.website.com/record/7
8	Record 8	666673	8	http://www.website.com/record/8
9	Record 9	666674	9	http://www.website.com/record/9
10	Record 10	666675	10	http://www.website.com/record/10
11	Record 11	666676	11	http://www.website.com/record/11
12	Record 12	666677	12	http://www.website.com/record/12
13	Record 13	666678	13	http://www.website.com/record/13
14	Record 14	666679	14	http://www.website.com/record/14
15	Record 15	666680	15	http://www.website.com/record/15
16	Record 16	666681	16	http://www.website.com/record/16
17	Record 17	666682	17	http://www.website.com/record/17
18	Record 18	666683	18	http://www.website.com/record/18
19	Record 19	666684	19	http://www.website.com/record/19
20	Record 20	666685	20	http://www.website.com/record/20
21	Record 21	666686	21	http://www.website.com/record/21
22	Record 22	666687	22	http://www.website.com/record/22
23	Record 23	666688	23	http://www.website.com/record/23
24	Record 24	666689	24	http://www.website.com/record/24
25	Record 25	666690	25	http://www.website.com/record/25
26	Record 26	666691	26	http://www.website.com/record/26
27	Record 27	666692	27	http://www.website.com/record/27
28	Record 28	666693	28	http://www.website.com/record/28
29	Record 29	666694	29	http://www.website.com/record/29
\.


--
-- Name: Artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Artist_id_seq"', 1, false);


--
-- Name: Record_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Record_id_seq"', 1, false);


--
-- Name: Artist Artist_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist"
    ADD CONSTRAINT "Artist_name_key" UNIQUE (name);


--
-- Name: Artist Artist_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artist"
    ADD CONSTRAINT "Artist_pkey" PRIMARY KEY (id);


--
-- Name: Record Record_isbn_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Record"
    ADD CONSTRAINT "Record_isbn_key" UNIQUE (isbn);


--
-- Name: Record Record_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Record"
    ADD CONSTRAINT "Record_pkey" PRIMARY KEY (id);


--
-- Name: Record Record_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Record"
    ADD CONSTRAINT "Record_artist_id_fkey" FOREIGN KEY (artist_id) REFERENCES public."Artist"(id);


--
-- PostgreSQL database dump complete
--

