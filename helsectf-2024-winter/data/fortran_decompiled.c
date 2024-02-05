void _init()
{
    if (false)
        0();
    return;
}

long long sub_401020()
{
    void* v0;  // [bp-0x8]

    v0 = 0;
}

long long _start()
{
    unsigned long v0;  // [bp-0x8]
    char v1;  // [bp+0x0]
    unsigned long v3;  // rax
    unsigned long long v4;  // rdx

    v0 = v3;
    __libc_start_main(main, *((long long *)&v1), &v1, __libc_csu_init, __libc_csu_fini, v4); /* do not return */
}

// No decompilation output for function sub_4010be

long long _dl_relocate_static_pie()
{
    unsigned long v1;  // rax

    return v1;
}

void deregister_tm_clones()
{
    if (true)
    {
        return;
    }
    else if (!(false))
    {
        return;
    }
}

long long register_tm_clones()
{
    if (true)
    {
        return 0;
    }
    else if (!(false))
    {
        return 0;
    }
}

extern char _edata;

long long __do_global_dtors_aux()
{
    unsigned long v0;  // [bp-0x8]
    unsigned long v2;  // rax

    if (!_edata)
    {
        *((int *)&v0) = rbp<8>;
        _edata = 1;
        return (unsigned long long)deregister_tm_clones();
    }
    return v2;
}

long long frame_dummy()
{
    return register_tm_clones();
}

extern void __a_MOD_flag;

void __a_MOD_b(void* a0, unsigned long a1, unsigned int *a2)
{
    unsigned long v0;  // [bp-0x18]

    v0 = a1;
    memmove(a0, "gemredsf|k3oFe`r1E2n`e02j_qqoh`MNdR8d_j^Fpqts`n`80~", 51);
    if (*(a2) > 0)
    {
        __a_MOD_d(a0, 51);
        return;
    }
    return;
}

void __a_MOD_d(unsigned long a0, unsigned long a1)
{
    unsigned int v0;  // [bp-0x238]
    unsigned int v1;  // [bp-0x234]
    unsigned long v2;  // [bp-0x230]
    unsigned int v3;  // [bp-0x228]
    unsigned long v4;  // [bp-0x1e8]
    unsigned long long v5;  // [bp-0x1e0]
    char v6;  // [bp-0x21]
    unsigned int v7;  // [bp-0x20]
    unsigned int v8;  // [bp-0x1c]
    unsigned long long v10;  // rcx
    unsigned long v11;  // rax

    for (v8 = 1; (unsigned int)a1 >= v8; v8 += 1)
    {
        v7 = *((char *)(a0 + v8 - 1));
        v2 = "main.f90";
        v3 = 19;
        v4 = "(a,$) is the real flag, not this: flag=";
        v5 = 5;
        v0 = 0x1000;
        v1 = 6;
        _gfortran_st_write(&v0);
        v10 = v8 - 1;
        v11 = (unsigned int)(((unsigned int)v10 ^ (unsigned int)(v8 - 1 >> 31)) * 1431655766 >> 32) ^ (unsigned int)(v8 - 1 >> 31);
        v6 = (char)v7 - ((char)v10 - ((char)((unsigned int)v11 * 2) + (char)v11) - 1);
        _gfortran_transfer_character_write(&v0, &v6, 1, &v6);
        _gfortran_st_write_done(&v0);
    }
    v2 = "main.f90";
    v3 = 21;
    v4 = "(a,$) is the real flag, not this: flag=";
    v5 = 5;
    v0 = 0x1000;
    v1 = 6;
    _gfortran_st_write(&v0);
    _gfortran_transfer_character_write(&v0, " is the real flag, not this: flag=", 29, v8 - 1);
    _gfortran_st_write_done(&v0);
    return;
}

extern unsigned int g_402040;

void MAIN__(unsigned long a0, unsigned long a1, unsigned long a2, unsigned long long a3)
{
    char v0;  // [bp-0x258]
    unsigned int v1;  // [bp-0x218]
    unsigned int v2;  // [bp-0x214]
    unsigned long v3;  // [bp-0x210]
    unsigned int v4;  // [bp-0x208]

    v3 = "main.f90";
    v4 = 34;
    v1 = 128;
    v2 = 6;
    _gfortran_st_write(&v1);
    _gfortran_transfer_character_write(&v1, "flag=", 5, a3);
    __a_MOD_b(&v0, 51, &g_402040);
    _gfortran_transfer_character_write(&v1, &v0, 51, &v0);
    _gfortran_st_write_done(&v1);
    return;
}

extern char options.5.0;

int main(unsigned long a0, unsigned long long a1, unsigned int a2, unsigned long long a3)
{
    _gfortran_set_args((unsigned int)a0, a1, a1);
    _gfortran_set_options(7, &options.5.0);
    MAIN__(7, &options.5.0, a2, a3);
    return 0;
}

long long __libc_csu_init(unsigned long long a0, unsigned long long a1, unsigned long long a2)
{
    unsigned long long v1;  // rax
    void* v2;  // rbx

    v1 = _init();
    if (false)
        return v1;
    v2 = 0;
    do
    {
        v1 = *((long long *)(4210128 + rbx<8> * 8))(a0, a1, a2);
        v2 += 1;
    } while (v2 != 1);
    return v1;
}

long long __libc_csu_fini()
{
    unsigned long v1;  // rax

    return v1;
}

long long _fini()
{
    unsigned long v1;  // rax

    return v1;
}

