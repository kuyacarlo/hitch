NAME = hitch
VERSION = 0.1.0
TARBALL = $(NAME)-$(VERSION).tar.gz

srpm:
	# Vendor Go dependencies
	go mod vendor

	# Create source tarball with vendored deps
	mkdir -p $(NAME)-$(VERSION)
	cp -a cmd internal main.go go.mod go.sum vendor testdata hitch.spec LICENSE Makefile $(NAME)-$(VERSION)/
	tar czf $(TARBALL) $(NAME)-$(VERSION)
	rm -rf $(NAME)-$(VERSION)

	# Build SRPM
	mkdir -p $(outdir)
	rpmbuild -bs hitch.spec \
		--define "_sourcedir $(CURDIR)" \
		--define "_srcrpmdir $(outdir)" \
		--define "gobuilddir ."
