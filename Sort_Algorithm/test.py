def func(a, b=2, c=5, *args, **kwargs):
    print 'a=%s' % a
    print 'b=%s' % b
    print 'c=%s' % c
    print 'args=', args
    print 'kwargs=', kwargs


if __name__ == "__main__":
    func(1, b=2, c=4, *(1111,),  name='helo')
