NAME = hitch
VERSION = 0.1.0
TARBALL = $(NAME)-$(VERSION).tar.gz
SRCDIR = $(shell cd .. && pwd)

srpm:
	# Create source tarball (vendor/ already committed in repo)
	cd $(SRCDIR) && \
	mkdir -p $(NAME)-$(VERSION) && \
	cp -a cmd internal main.go go.mod go.sum vendor testdata hitch.spec LICENSE Makefile .gitignore $(NAME)-$(VERSION)/ && \
	tar czf $(TARBALL) $(NAME)-$(VERSION) && \
	rm -rf $(NAME)-$(VERSION)

	# Build SRPM
	rpmbuild -bs $(SRCDIR)/hitch.spec \
		--define "_sourcedir $(SRCDIR)" \
		--define "_srcrpmdir $(outdir)"
